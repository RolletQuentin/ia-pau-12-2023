<template>
    <FormWrapper>
        <form>
            <div>
                <h2>Votre compétence</h2>

                <label for="skills">Vos ou votre compétence(s)</label>
                <textarea v-model="skills" id="skills" required></textarea>

                <label for="examples">Appliquée(s) dans quel contexte, des exemples ?</label>
                <textarea v-model="examples" type="text" id="examples" required />
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
        const skills = ref('')
        const examples = ref('')

        const lastName = ref('')
        const firstName = ref('')
        const phone = ref('')
        const email = ref('')
        const city = ref('')

        function submitForm() {
            const data = {
                skills: skills.value,
                examples: examples.value,
                lastName: lastName.value,
                firstName: firstName.value,
                phone: phone.value,
                email: email.value,
                city: city.value
            }
            fetch('http://localhost:8000/create-project-holder', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
        }

        return {
            skills,
            examples,
            lastName,
            firstName,
            phone,
            email,
            city,
            submitForm
        }
    }
}
</script>
