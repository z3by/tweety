import { ref } from "vue";

const useFocus = () => {
  const isFocused = ref<boolean>(false);
  const focus: () => void = () => {
    isFocused.value = true;
  };
  const blur: () => void = () => {
    isFocused.value = false;
  };
  return { isFocused, focus, blur };
};

export default useFocus;
