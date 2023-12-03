<template>
    <FormWrapper>
        <form>
            <div>
                <label for="identifiant">Identifiant</label>
                <input type="text" v-model="identifiant" id="identifiant" required />
            </div>
        </form>
        <button @click="submitForm">Envoyer</button>
    </FormWrapper>
</template>

<script lang="ts">
import FormWrapper from '@/components/Forms/FormWrapper.vue'
import { ref } from 'vue'

export default {
    components: {
        FormWrapper
    },
    setup() {
        const identifiant = ref('')

        function submitForm() {
            const data = {
                id: identifiant.value
            }
            fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then((response) => response.json())
                .then((data) => console.log(data))
                .catch((error) => console.error(error))
        }

        return {
            identifiant,
            submitForm
        }
    }
}
</script>
