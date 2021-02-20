<template>
  <div id="myApp">
    <div class="container mt-4">
      <div class="row justify-content-md-center">
        <div class="col-md-8">
          <div class="card">
            <div class="card-header text-center bg-dark text-light">
              <h4>{{name}}'s LOG LIST</h4>
            </div>
          </div>
        </div>
      </div>
    </div>


   
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      name:'Nill'
    }
  }
 
}
</script>

<style>
body{
  background-color: antiquewhite;
}

</style>
