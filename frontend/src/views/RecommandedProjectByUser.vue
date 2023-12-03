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
