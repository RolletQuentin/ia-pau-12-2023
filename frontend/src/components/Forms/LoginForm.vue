<template>
    <FormWrapper>
        <form>
            <div>
                <label for="id">Identifiant</label>
                <input v-model="id" id="id" />
            </div>
            <button :onclick="submitForm">Envoyer</button>
        </form>
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
        const id = ref('')

        function submitForm() {
            const data = {
                id: id.value
            }
            fetch('http://localhost:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }

        return {
            id,
            submitForm
        }
    }
}
</script>
