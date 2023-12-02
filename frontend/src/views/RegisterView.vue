<template>
    <div>
        <h1>Nous rejoindre</h1>

        <!-- <h2>Inscription</h2>

        <RegisterForm /> -->

        <h2>Se connecter</h2>

        <LoginForm />

        <h2>Nouveau projet</h2>

        <ProjectForm />

        <!-- <h2>Porteurs bénévoles de compétences</h2>

        <SkillsForm /> -->
    </div>
</template>

<script lang="ts" scoped>
import ProjectForm from '@/components/Forms/ProjectForm.vue'
// import SkillsForm from '@/components/Forms/SkillsForm.vue'
// import RegisterForm from '@/components/Forms/RegisterForm.vue'
import LoginForm from '@/components/Forms/LoginForm.vue'

export default {
    components: {
        ProjectForm,
        // SkillsForm,
        // RegisterForm,
        LoginForm
    }
}
</script>
