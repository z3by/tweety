<template>
  <div class="signup">
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
          <h3 class="text-2xl">Create your account</h3>
          <form>
            <Input v-model="name" name="Name" type="text" />
            <Input v-model="phone" v-if="usePhone" name="Phone" type="text" />
            <Input v-model="email" v-else name="Email" type="email" />
            <Button
              @click.prevent="usePhone = !usePhone"
              class="mt-4"
              type="text"
            >
              Use {{ usePhone ? "email" : "phone" }} instead
            </Button>

            <div class="mt-8">
              <h6>Date of birth</h6>
              <p class="text-normal text-cool-gray-600 font-normal">
                This will not be shown publicly. Confirm your own age, even if
                this account is for a business, a pet, or something else.
              </p>
              <div class="flex gap-3">
                <Select
                  name="Month"
                  class="w-1/3"
                  :options="months"
                  v-model="birthdayMonth"
                />
                <Select
                  name="Day"
                  class="w-1/5"
                  :options="days"
                  v-model="birthdayDay"
                />
                <Select
                  name="Year"
                  class="w-1/5"
                  :options="years"
                  v-model="birthdayYear"
                />
              </div>
            </div>
            <div class="pt-3 pb-9">
              <Button class="w-full mt-5 h-11" :disabled="false"
                >Sign up</Button
              >
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>

<script lang="ts" setup>
import Input from "@/components/Input.vue";
import Button from "@/components/Button.vue";
import { computed, ref } from "@vue/reactivity";
import Select from "@/components/Select.vue";
import { Option } from "@/types";

const name = ref<string>("");
const email = ref<string>("");
const phone = ref<string>("");
const birthdayYear = ref<string>("");
const birthdayMonth = ref<string>("");
const birthdayDay = ref<string>("");
const usePhone = ref<boolean>(false);

const months: Option[] = [
  { text: "January", value: "1" },
  { text: "February", value: "2" },
  { text: "March", value: "3" },
  { text: "April", value: "4" },
  { text: "May", value: "5" },
  { text: "June", value: "6" },
  { text: "July", value: "7" },
  { text: "August", value: "8" },
  { text: "September", value: "9" },
  { text: "October", value: "10" },
  { text: "November", value: "11" },
  { text: "December", value: "12" },
];
const days = computed(() => {
  const daysList: Option[] = [];
  // the default if the user didn't select the year nor the month
  let numOfDaysInMonth = 31;
  // if the user selected the year and the month we calculate how many days in that month
  if (birthdayMonth.value && birthdayYear.value) {
    numOfDaysInMonth = new Date(
      ~~birthdayYear.value,
      ~~birthdayMonth.value,
      0
    ).getDate();
  } else if (
    // if the user selected only the month and specified it as February we limit the number to 29
    birthdayMonth.value &&
    !birthdayYear.value &&
    birthdayMonth.value == "2"
  ) {
    numOfDaysInMonth = 29;
  }
  for (let i = 1; i <= numOfDaysInMonth; i++) {
    daysList.push({ value: i, text: i.toString() });
  }
  return daysList;
});

const currentYear = new Date().getFullYear();
const years: Option[] = [];
for (let i = 0; i < 120; i++) {
  const year = currentYear - i;
  years.push({ value: year, text: year.toString() });
}
</script>
