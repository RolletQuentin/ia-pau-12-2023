<template>
    <h1>Recommandation d'un projet avec un projet</h1>

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
        <div v-for="project in data.projects" v-bind:key="project.id">
            <h2>{{ project.name }}</h2>
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
            fetch('http://localhost:8000/project-recommandation/', {
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
