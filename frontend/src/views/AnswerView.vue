<template>
  <div class="answer">
    <button v-on:click="getAnswer">What is the answer?</button>
    <p>{{ answer }}</p>
  </div>
</template>

<script lang="ts">
import axios from 'axios';

export default {
  name: 'AnswerDisplay',
  data() {
    return {
      answer: null
    };
  },
  methods: {
    getAnswer() {
      axios.get('http://localhost:8000/answer')
        .then(response => {
          this.answer = response.data.answer;
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
}

</script>

<style>
</style>
