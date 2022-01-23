<template>
  <div
    class="floating-label-input relative rounded-md border focus-within:border-sky-500 focus-within:border-1 my-5 cursor-pointer"
  >
    <input
      :id="name"
      :type="type"
      :placeholder="name"
      :value="modelValue"
      :maxlength="maxlength"
      @focus="focus"
      @blur="blur"
      @input="input"
      class="w-full px-3 pb-2 pt-6 outline-none rounded-md text-lg placeholder-transparent"
    />
    <label
      :for="name"
      class="absolute left-0 transition-all duration-200 mx-3 font-normal"
      :class="labelClasses"
      >{{ name }}</label
    >
  </div>
</template>

<script setup lang="ts">
import { computed, defineEmits, defineProps } from "vue";
import useFocus from "@/composables/useFocus";

const { isFocused, focus, blur } = useFocus();

interface Props {
  type: string;
  name: string;
  modelValue?: string;
  maxlength?: number;
}

const props = defineProps<Props>();

interface Emits {
  (e: "update:modelValue", value: string): void;
}
const emit = defineEmits<Emits>();

const labelClasses = computed(() => {
  const classes = [];
  if (isFocused.value) {
    classes.push("text-sky-500", "text-sm", "top-1");
  } else if (props.modelValue) {
    classes.push("text-cool-gray-500", "text-sm", "top-1");
  } else {
    classes.push("text-cool-gray-500", "text-lg", "top-4");
  }
  return classes;
});
const input = ($event: Event) => {
  const inputEl = $event.target as HTMLInputElement;
  emit("update:modelValue", inputEl.value);
};
</script>
