<template>
    <h1>Recommandation de projets pour un projet</h1>

    <FormWrapper>
        <form>
            <div>
                <label for="projectName">Nom du projet</label>
                <input type="text" id="projectName" v-model="projectName" />
            </div>
        </form>
        <button :onclick="submitForm">Envoyer</button>
    </FormWrapper>

    <div v-if="isLoaded" class="data-visualization">
        <div v-for="project in data" v-bind:key="project.ID">
            <h2>{{ project['Nom du Projet'] }}</h2>

            <h3>Description :</h3>
            <p>{{ project['Description du projet'] }}</p>

            <h3>Recommandation</h3>
            <p>
                Ce projet vous est recommandé à
                {{ Math.floor(project.recommendation.coef * 100) }} %
            </p>
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

<style scoped>
.data-visualization {
    h3 {
        font-size: 1.25em;
        font-weight: 300;
        margin-bottom: 5px;
    }
}
</style>
