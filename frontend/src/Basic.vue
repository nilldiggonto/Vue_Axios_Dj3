<template>
  <div id="myApp">
    <div class="container mt-4">
      <div class="row justify-content-md-center">
        <div class="col-md-8">

          <div class="row">
            <div class="col-md-12 text-center">
              <input type="text" v-model="newItemText" class="form-control">
              <button class="btn btn-primary mt-1" v-on:click="addNewLog">Add+ Log</button>
            </div>
            <!-- <div class="col">
              <input type="text" v-model="newItemText" class="form-control">
            </div> -->
          </div>



          <div class="card">
            <div class="card-header text-center bg-dark text-light">
              <h4>{{ name }}'s LOG LIST</h4>
              <input type="checkbox" v-model="hide" class="form-check-input">
              <label for="">Hide</label>
              <br />

              <div
                class="row d-flex justify-content-between px-2 py-2"
                v-for="l in hiddenList"
                v-bind:key="l.list"
              >
                <div >
                  <p>{{ l.task }}</p>
                </div>

                <div>
                  <input type="checkbox" v-model="l.complete" class="form-check-input">                   <!-- <label for=""></label> -->
                </div>

             
              </div> <!--d-flex-->

              


            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// export default {
//   name: "App",
//   data() {
//     return {
//       name: "Nill",
//       list: [
//         { task: "API build", complete: false },
//         { task: "New project", complete: false },
//         { task: "Exercise", complete: false },
//       ],
//       hide:true,
//       newItemText:"",
//     };
//   },
//   computed:{
//     hiddenList(){
//       return this.hide? this.list.filter(l=> !l.complete): this.list
//     }
//   },
//   methods:{
//     addNewLog(){
//       this.list.push({
//         task: this.newItemText,
//         complete:false
//       });
//       this.newItemText = "";
//     }
// //   }
// };
</script>

<style>
body {
  background-color: antiquewhite;
}
</style>
