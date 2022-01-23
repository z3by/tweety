<template>
  <button :class="buttonClasses" :disabled="disabled" :aria-disabled="disabled">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import { computed, defineProps } from "vue";

interface Props {
  type?: string;
  disabled?: boolean;
}
const props = defineProps<Props>();

const buttonClasses = computed(() => {
  const classes = [];
  if (props.type === "text") {
    classes.push("text-sky-500");
  } else {
    classes.push(
      "py-2",
      "px-5",
      "text-lg",
      "bg-black",
      "text-white",
      "rounded-full",
      "font-bold"
    );
  }
  if (props.disabled) {
    classes.push("!bg-gray-400", "text-gray-200", "cursor-not-allowed");
  }
  return classes;
});
</script>
