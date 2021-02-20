<template>
  <div class="posts">
    <Navbar></Navbar>
    <!-- <h4>This is the post page</h4> -->
    <div class="container-fluid">
      <div v-for="posts in APIData" :key="posts.id">
        <div class="card border-primary mb-3 mt-2" style="max-width: 20rem">
          <div class="card-header">{{posts.title}}}}</div>
          <div class="card-body">
            <h4 class="card-title">Primary card title</h4>
            <p class="card-text">
              {{posts.content}}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getAPI} from '../axios-api'
import Navbar from "../components/Navbar";
export default {
  name: "Posts",
  data(){
      return{
          APIData: []
      }
  },

  components: {
    Navbar,
  },
  created(){
      getAPI.get('/posts/',)
      .then(response=>{
          console.log('DATA received')
          this.APIData = response.data
      })
      .catch(err=>{
          console.log(err)
      })
  }
};
</script>

<style scoped>
</style>