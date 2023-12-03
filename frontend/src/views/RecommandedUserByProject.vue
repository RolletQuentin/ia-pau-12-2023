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
            <p>Utilisateur recommandé à {{ Math.floor(user.recommendation.coef * 100) }} %</p>
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
