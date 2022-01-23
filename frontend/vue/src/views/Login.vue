<template>
  <div class="login">
    <main class="h-screen bg-gray-400 flex justify-center items-center">
      <div
        class="modal h-screen md:h-screen-sm w-screen md:w-xl bg-white mx-auto rounded-2xl"
      >
        <div class="modal-header p-2 flex">
          <router-link
            to="/"
            class="h-10 w-10 hover:bg-light-600 active:bg-gray-300 text-2xl rounded-full flex items-center justify-center"
          >
            <i class="bi-x"></i>
          </router-link>
          <div class="flex justify-center flex-1">
            <img
              src="@/assets/img/tweety-logo.svg"
              alt="Tweety logo"
              class="h-10 w-10"
            />
          </div>
        </div>
        <div class="modal-body py-6 px-8 font-bold">
          <h3 class="text-2xl">Sign in to Tweety</h3>
          <form>
            <Input
              v-model="userId"
              name="Phone, email or user name"
              type="text"
            />
            <Input v-model="password" name="Password" type="password" />
            <Button class="w-full mt-5" :disabled="false">Log in</Button>
          </form>
          <p class="font-normal my-8 block text-cool-gray-600">
            Don't have an account?
            <router-link to="/signup" class="text-sky-600">Sign up</router-link>
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts" setup>
import Input from "@/components/Input.vue";
import Button from "@/components/Button.vue";
import { ref } from "@vue/reactivity";

const userId = ref<string>("");
const password = ref<string>("");
</script>
