<template>
    <h1>Recommandation des utilisateurs pour un projet</h1>

    <FormWrapper>
        <form>
            <div>
                <label for="projectName">Nom du projet</label>
                <input type="text" id="projectName" v-model="projectName" />
            </div>
        </form>
        <button @click="submitForm">Envoyer</button>
    </FormWrapper>

    <div v-if="isLoaded" class="data-visualization">
        <div v-for="user in data" v-bind:key="user.ID">
            <h2>ID de l'utilsateur : {{ user.ID }}</h2>

            <h3>Compétences :</h3>
            <p>{{ user.Compétences }}</p>

            <h3>Recommandation</h3>
            <p>
                Cet utilisateur vous est recommandé à
                <strong>{{ Math.floor(user.recommendation.coef * 100) }} %</strong>
            </p>
            <p>En effet, cet utilisateur vous est recommandé pour :</p>
            <ul>
                <li v-if="user.recommendation.coef_proximite_geographique > 0.5">
                    Sa proximité géographique :
                    <strong
                        >{{
                            Math.floor(user.recommendation.coef_proximite_geographique * 100)
                        }}
                        %</strong
                    >
                </li>
                <li v-if="user.recommendation.coef_champ_lexical > 0.5">
                    Son champ lexical :
                    <strong
                        >{{ Math.floor(user.recommendation.coef_champ_lexical * 100) }} %</strong
                    >
                </li>
                <li v-if="user.recommendation.coef_flux_matiere > 0.5">
                    Son flux de matière :
                    <strong>{{ Math.floor(user.recommendation.coef_flux_matiere * 100) }} %</strong>
                </li>
                <li v-if="user.recommendation.coef_flux_competence > 0.5">
                    Son flux de compétences :
                    <strong
                        >{{ Math.floor(user.recommendation.coef_flux_competence * 100) }} %</strong
                    >
                </li>
                <li v-if="user.recommendation.coef_domain_application > 0.5">
                    Son domaine d'application :
                    <strong
                        >{{
                            Math.floor(user.recommendation.coef_domain_application * 100)
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
        const projectName = ref('')
        const data = ref()
        const isLoaded = ref(false)

        function submitForm() {
            fetch('http://localhost:8000/links-projet-with-users/', {
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
                    console.log(data.value)
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
