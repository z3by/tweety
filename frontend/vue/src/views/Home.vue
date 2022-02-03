<template>
  <div class="home flex h-screen justify-center">
    <header role="banner" class="border-r border-light-400">
      <Sidebar />
    </header>
    <main class="max-w-[600px] flex-1">
      <Navbar />
      <TweetInput />
      <Timeline />
    </main>
  </div>
</template>

<script setup lang="ts">
import Sidebar from "@/components/home/Sidebar.vue";
import Timeline from "@/components/home/Timeline.vue";
import TweetInput from "@/components/home/TweetInput.vue";
import Navbar from "@/components/home/Navbar.vue";
</script>
