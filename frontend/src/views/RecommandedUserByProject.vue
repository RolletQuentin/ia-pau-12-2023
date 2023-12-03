<template>
    <h1>Recommandation des utilisateurs pour un projet</h1>

    <FormWrapper>
        <form>
            <div>
                <label for="projectName">Nom du projet</label>
                <input type="text" id="projectName" v-model="projectName" />
            </div>
        </form>
        <button :onclick="submitForm">Envoyer</button>
    </FormWrapper>

    <div v-if="isLoaded">
        <div v-for="user in data.users" v-bind:key="user.id">
            <h2>{{ user.name }}</h2>
        </div>
    </div>
</template>

<script lang="ts">
import FormWrapper from '@/components/Forms/FormWrapper.vue'
import { ref } from 'vue'

export default {
    components: {
        FormWrapper
    },
    setup() {
        const projectName = ref('')
        const data = ref()
        const isLoaded = ref(false)

        function submitForm() {
            fetch('http://localhost:8000//links-projet-with-users/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nom_du_projet: projectName.value
                })
            })
                .then((response) => response.json())
                .then((responseData) => {
                    data.value = responseData
                    isLoaded.value = true
                })
                .catch((error) => console.error(error))
        }

        return {
            projectName,
            isLoaded,
            data,
            submitForm
        }
    }
}
</script>
