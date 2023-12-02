<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from '@/components/HeaderBase.vue'
import Footer from '@/components/FooterBase.vue'
</script>

<template>
    <div id="page">
        <Header> </Header>

        <main>
            <RouterView />
        </main>
        <Footer></Footer>
    </div>
</template>

<style lang="scss" scoped>
#page {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

main {
    padding: 10px 50px;
    margin-bottom: 30px;
    flex: 1;
}
</style>
