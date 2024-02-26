<template>
  <div>
    <!-- Wrap the content inside a button element -->
    <button @click="getNewAnswer" style="cursor: pointer;">The answer is: </button>
    <p>{{ answer }}</p>
  </div>
</template>

<script>
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
    getNewAnswer() {
      // This method is called when the button is clicked
      this.getAnswer(); // Call the getAnswer method to fetch a new answer
    }
  }
}
</script>

<style scoped>
div {
  text-align: center;
}
</style>
