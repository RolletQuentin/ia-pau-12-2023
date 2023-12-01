<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from '@/components/HeaderBase.vue'
import Footer from '@/components/FooterBase.vue'
</script>

<template>
    <div id="page">
        <Header> </Header>

        <RouterView />

        <Footer></Footer>
    </div>
</template>

<style lang="scss">
#page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
</style>
