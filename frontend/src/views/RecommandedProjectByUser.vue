<template>
    <h1>Recommandation de projets pour un utilisateur</h1>

    <FormWrapper>
        <form>
            <div>
                <label for="userid">ID de l'utilisateur</label>
                <input type="text" id="userid" v-model="userid" />
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
                <strong>{{ Math.floor(project.recommendation.coef * 100) }} %</strong>
            </p>
            <p>En effet, ce projet vous est recommandé pour :</p>
            <ul>
                <li v-if="project.recommendation.coef_proximite_geographique > 0.5">
                    Sa proximité géographique :
                    <strong
                        >{{
                            Math.floor(project.recommendation.coef_proximite_geographique * 100)
                        }}
                        %</strong
                    >
                </li>
                <li v-if="project.recommendation.coef_champ_lexical > 0.5">
                    Son champ lexical :
                    <strong
                        >{{ Math.floor(project.recommendation.coef_champ_lexical * 100) }} %</strong
                    >
                </li>
                <li v-if="project.recommendation.coef_flux_matiere > 0.5">
                    Son flux de matière :
                    <strong
                        >{{ Math.floor(project.recommendation.coef_flux_matiere * 100) }} %</strong
                    >
                </li>
                <li v-if="project.recommendation.coef_flux_competence > 0.5">
                    Son flux de compétences :
                    <strong
                        >{{
                            Math.floor(project.recommendation.coef_flux_competence * 100)
                        }}
                        %</strong
                    >
                </li>
                <li v-if="project.recommendation.coef_domain_application > 0.5">
                    Son domaine d'application :
                    <strong
                        >{{
                            Math.floor(project.recommendation.coef_domain_application * 100)
                        }}
                        %</strong
                    >
                </li>
            </ul>
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
        const userid = ref('')
        const data = ref()
        const isLoaded = ref(false)

        function submitForm() {
            fetch('http://localhost:8000/links-user-with-projets/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    id: userid.value
                })
            })
                .then((response) => response.json())
                .then((responseData) => {
                    data.value = responseData
                    console.log(data.value)
                    isLoaded.value = true
                })
                .catch((error) => console.error(error))
        }

        return {
            userid,
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
        margin: 10px 0px;
    }
}
</style>
