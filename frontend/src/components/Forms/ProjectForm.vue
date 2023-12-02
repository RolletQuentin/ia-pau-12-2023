<template>
    <FormWrapper>
        <form>
            <div>
                <h2>Votre projet</h2>

                <label for="projectTitle">Titre du projet</label>
                <input v-model="projectTitle" type="text" id="projectTitle" required />

                <label for="maturityStage">Stade de maturité</label>
                <div>
                    <label v-for="(stage, index) in maturityStages" :key="index">
                        <input
                            type="radio"
                            v-model="maturityStage"
                            :value="stage"
                            :id="'maturityStage_' + index"
                            required
                        />
                        {{ stage }}
                    </label>
                </div>

                <label for="projectNeeds">Besoins du projet</label>
                <textarea v-model="projectNeeds" id="projectNeeds" required></textarea>

                <label for="projectOffer">Offre accompagnant le projet</label>
                <textarea v-model="projectOffer" type="text" id="projectOffer" required />

                <label for="circularityForm">Forme de circularité</label>
                <textarea v-model="circularityForm" id="circularityForm" required></textarea>
            </div>

            <div>
                <h2>Vos coordonnées</h2>

                <label for="lastName">Nom</label>
                <input v-model="lastName" type="text" id="lastName" required />

                <label for="firstName">Prénom</label>
                <input v-model="firstName" type="text" id="firstName" required />

                <label for="phone">Téléphone</label>
                <input v-model="phone" type="tel" id="phone" required />

                <label for="email">Mail</label>
                <input v-model="email" type="email" id="email" required />

                <label for="city">Ville</label>
                <input v-model="city" type="text" id="city" required />
            </div>

            <button type="submit">Envoyer</button>
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
        const projectTitle = ref('')
        const maturityStages = ref([
            "1-Graine (L'idée)",
            '2-Plant (Busisness model et business plan)',
            '3-Fleur (Proof of concept)',
            '4-Fruit (Commercialisation)'
        ])
        const maturityStage = ref()
        const projectNeeds = ref('')
        const projectOffer = ref('')
        const circularityForm = ref('')

        const lastName = ref('')
        const firstName = ref('')
        const phone = ref('')
        const email = ref('')
        const city = ref('')

        return {
            projectTitle,
            maturityStages,
            maturityStage,
            projectNeeds,
            projectOffer,
            circularityForm,
            lastName,
            firstName,
            phone,
            email,
            city
        }
    }
}
</script>
