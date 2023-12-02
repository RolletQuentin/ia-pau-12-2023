<template>
    <div>
        <h1>Nous rejoindre</h1>

        <h2>Porteurs de projets</h2>

        <ProjectForm />

        <h2>Porteurs bénévoles de compétences</h2>

        <SkillsForm />
    </div>
</template>

<script lang="ts" scoped>
import ProjectForm from '@/components/Forms/ProjectForm.vue'
import SkillsForm from '@/components/Forms/SkillsForm.vue'

export default {
    components: {
        ProjectForm,
        SkillsForm
    }
}
</script>
