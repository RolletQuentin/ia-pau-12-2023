<template>
    <FormWrapper>
        <form>
            <div>
                <label for="wish">Pourquoi as-tu eu envie de rejoindre HBN ?</label>
                <textarea v-model="wish" id="wish" required></textarea>

                <label for="role">Quel y sera ton rôle ?</label>
                <textarea v-model="role" type="text" id="role" required />

                <label for="skills">Compétences</label>
                <input v-model="skills" id="skills" />

                <label for="circular-skills">Compétences en circularité</label>
                <input type="text" v-model="circularSkills" id="circular-skills" />

                <label for="skills-family">Familles de compétences</label>
                <input text="" />

                <label for="additionnal-skills">Compétences à ajouter</label>
                <input type="text" v-model="additionnalSkills" id="additionnal-skills" />

                <label for="material">Matériel</label>
                <input type="text" v-model="material" id="material" />

                <label for="circular-material">Matériel en circularité</label>
                <input type="text" v-model="circularMaterial" id="circular-material" />

                <label for="additionnal-material">Matériel à ajouter</label>
                <input type="text" v-model="additionnalMaterial" id="additionnal-material" />

                <label for="raw-material">Matières</label>
                <input type="text" v-model="rawMaterial" id="raw-material" />

                <label for="new-raw-material">Matières</label>
                <input type="text" v-model="newRawMaterial" id="new-raw-material" />
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

                <label for="cp">Code postal</label>
                <input v-model="cp" type="text" id="cp" required />
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
        const wish = ref('')
        const role = ref('')
        const skills = ref('')
        const circularSkills = ref('')
        const additionnalSkills = ref('')
        const material = ref('')
        const circularMaterial = ref('')
        const additionnalMaterial = ref('')
        const rawMaterial = ref('')
        const newRawMaterial = ref('')

        const lastName = ref('')
        const firstName = ref('')
        const phone = ref('')
        const email = ref('')
        const city = ref('')
        const cp = ref('')

        function submitForm() {
            const data = {
                wish: wish.value,
                role: role.value,
                skills: skills.value,
                circularSkills: circularSkills.value,
                additionnalSkills: additionnalSkills.value,
                material: material.value,
                circularMaterial: circularMaterial.value,
                additionnalMaterial: additionnalMaterial.value,
                rawMaterial: rawMaterial.value,
                newRawMaterial: newRawMaterial.value,
                lastName: lastName.value,
                firstName: firstName.value,
                phone: phone.value,
                email: email.value,
                city: city.value,
                cp: cp.value
            }
            fetch('http://localhost:8000/create-project', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }

        return {
            wish,
            role,
            skills,
            circularSkills,
            additionnalSkills,
            material,
            circularMaterial,
            additionnalMaterial,
            rawMaterial,
            newRawMaterial,
            lastName,
            firstName,
            phone,
            email,
            city,
            cp,
            submitForm
        }
    }
}
</script>
