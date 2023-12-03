<template>
    <FormWrapper>
        <form>
            <div>
                <label for="projectTitle">Titre du projet</label>
                <input v-model="projectTitle" type="text" id="projectTitle" required />

                <label for="projectDescription">Description</label>
                <textarea v-model="projectDescription" id="projectDescription" required></textarea>

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

                <label for="projectNeeds">Quels sont tes besoins actueles ?</label>
                <textarea v-model="projectNeeds" id="projectNeeds" required></textarea>

                <label for="activityDomain">Domaine d'activité</label>
                <input v-model="activityDomain" type="text" id="activityDomain" required />

                <label for="projectCity">Lieu du projet</label>
                <input v-model="projectCity" type="text" id="projectCity" required />

                <label for="cp">Code postal du projet</label>
                <input v-model="cp" type="text" id="cp" required />

                <label for="maturityStage">ODD fixé par l'ONU</label>
                <div>
                    <label v-for="(odd, index) in listOdd" :key="index">
                        <input
                            type="checkbox"
                            v-model="listChosenOdd"
                            :value="odd"
                            :id="'odd_' + index"
                        />
                        {{ odd }}
                    </label>
                </div>

                <label for="inMaterials">Matières entrantes</label>
                <input v-model="inMaterials" type="text" id="inMaterials" required />

                <label for="coproducts">Coproduits</label>
                <input v-model="coproducts" type="text" id="coproducts" required />
            </div>
        </form>
        <button :onclick="submitForm">Envoyer</button>
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
        const projectDescription = ref('')
        const maturityStages = ref([
            'Projet à reprendre!',
            "1 - Graine (L'idée)",
            '2 - Plant (Le business model)',
            '3 - Fleur (Le prototype)',
            '4 - Fruit (La commercialisation)'
        ])
        const maturityStage = ref()
        const projectNeeds = ref('')
        const activityDomain = ref('')
        const projectCity = ref('')
        const cp = ref('')
        const listOdd = ref([
            '1-Pas de pauvreté',
            '2-Zéro faim',
            '3-Bonne santé et bien-être',
            '4-Education de qualité',
            '5-Égalité entre les sexes',
            '6-Eau propre assainissement',
            "7-Energie propre et d'un coût abordable",
            '8-Travail décent et croissance économique',
            '9-Industrie, innovation et infrastructure',
            '10-Inégalités réduites',
            '11-Villes et communautés durable',
            '12-Consommation et production responsables',
            '13-Mesures relatives à la lutte contre les changements climatiques',
            '14-Vie aquatique',
            '15-Vie terrestre',
            '16-Paix, justice et institutions efficaces',
            '17-Partenariats pour la réalisation des objectifs'
        ])
        const listChosenOdd = ref([])
        const inMaterials = ref('')
        const coproducts = ref('')

        function submitForm() {
            const data = {
                nom_du_projet: projectTitle.value,
                description_du_projet: projectDescription.value,
                maturite_du_projet: maturityStage.value,
                besoins_actuels: projectNeeds.value,
                domaine_activite: activityDomain.value,
                lieu_du_projet: projectCity.value,
                code_postal: cp.value,
                odd: listChosenOdd.value,
                matieres_entrantes: inMaterials.value,
                coproduits: coproducts.value
            }
            fetch('http://localhost:8000/create-project/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }

        return {
            projectTitle,
            projectDescription,
            maturityStages,
            maturityStage,
            projectNeeds,
            activityDomain,
            projectCity,
            cp,
            listOdd,
            listChosenOdd,
            inMaterials,
            coproducts,
            submitForm
        }
    }
}
</script>
