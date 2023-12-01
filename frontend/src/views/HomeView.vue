<template>
    <main>
        <h2>Hello World from Vue!</h2>
        <h2>{{ welcomeMessage }}</h2>
    </main>
</template>

<script lang="ts">
import { ref } from 'vue'

export default {
    setup() {
        const welcomeMessage = ref('')
        fetch('http://localhost:8000/')
            .then((response) => response.json())
            .then((data) => (welcomeMessage.value = data.message))
            .catch((error) => console.error(error))

        return {
            welcomeMessage
        }
    }
}
</script>

<style lang="scss">
main {
    border: 1px solid red;
    flex: 1;
}
</style>
