<template>
  <div
    class="rounded-lg border focus-within:border-sky-500 focus-within:border-1 my-5 z-1"
  >
    <label
      :for="name"
      class="text-sm font-normal absolute px-3 py-1 -z-1"
      :class="isFocused ? 'text-sky-500' : 'text-cool-gray-600'"
      >{{ name }}</label
    >
    <select
      class="w-full rounded-lg outline-transparent h-full pb-2 pt-6 pl-2 pr-5 z-0 bg-transparent"
      :id="name"
      :value="modelValue"
      @focus="focus"
      @blur="blur"
      @input="input"
    >
      <option value="" disabled selected></option>
      <option
        v-for="option in options"
        :value="option.value"
        :key="option.value"
      >
        {{ option.text }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import useFocus from "@/composables/useFocus";
import { Option } from "@/types";

const { isFocused, focus, blur } = useFocus();

interface Props {
  name?: string;
  options: Option[];
  modelValue: string;
}
const props = defineProps<Props>();

interface Emits {
  (e: "update:modelValue", value: string): void;
}
const emit = defineEmits<Emits>();

const input = ($event: Event) => {
  const target = $event.target as HTMLSelectElement;
  emit("update:modelValue", target.value);
};
</script>
