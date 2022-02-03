<template>
  <button :class="buttonClasses" :disabled="disabled" :aria-disabled="disabled">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import { computed, defineProps } from "vue";

interface Props {
  type?: "primary" | "text" | "secondary";
  disabled?: boolean;
}
const props = defineProps<Props>();

const buttonClasses = computed(() => {
  const classes = [];
  const primaryClasses = [
    "py-2",
    "px-5",
    "rounded-full",
    "font-bold",
    "text-lg",
    "bg-black",
    "text-white",
    "hover:bg-gray-900",
    "active:bg-gray-800",
  ];
  const disabledClasses = [
    "!bg-gray-400",
    "text-gray-200",
    "cursor-not-allowed",
  ];
  if (props.type === "text") {
    classes.push("text-sky-500");
  }
  if (props.type === "primary" || props.type === undefined) {
    classes.push(...primaryClasses);
  }
  if (props.disabled) {
    classes.push(...disabledClasses);
  }
  return classes;
});
</script>
