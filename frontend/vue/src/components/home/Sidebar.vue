<template>
  <div class="sidebar px-3">
    <nav class="w-16 lg:w-64">
      <div class="tweety-logo my-1">
        <router-link
          to="/home"
          class="hover:bg-sky-100 inline-block rounded-full p-2 w-[50px] h-[50px]"
        >
          <img
            src="@/assets/img/tweety-logo.svg"
            alt="Tweety logo"
            class="w-full"
          />
        </router-link>
      </div>
      <ul>
        <li class="py-1">
          <router-link
            to="/home"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <HomeIconFill
                class="inline h-7"
                v-if="currentActive === 'home'"
              />
              <HomeIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'home' }"
              >
                Home
              </span>
            </div>
          </router-link>
        </li>

        <li class="py-1">
          <router-link
            to="/explore"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <ExploreIconFill
                class="inline h-7"
                v-if="currentActive === 'explore'"
              />
              <ExploreIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'explore' }"
              >
                Explore
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/notifications"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <NotificationsIconFill
                class="inline h-7"
                v-if="currentActive === 'notifications'"
              />
              <NotificationsIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'notifications' }"
              >
                Notifications
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/messages"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <MessagesIconFill
                class="inline h-7"
                v-if="currentActive === 'messages'"
              />
              <MessagesIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'messages' }"
              >
                Messages
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/bookmarks"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <BookmarksIconFill
                class="inline h-7"
                v-if="currentActive === 'bookmarks'"
              />
              <BookmarksIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'bookmarks' }"
              >
                Bookmarks
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/lists"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <ListsIconFill
                class="inline h-7"
                v-if="currentActive === 'lists'"
              />
              <ListsIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'lists' }"
              >
                Lists
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/profile"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <ProfileIconFill
                class="inline h-7"
                v-if="currentActive === 'profile'"
              />
              <ProfileIconOutline class="inline h-7" v-else />

              <span
                class="hidden lg:inline text-xl ml-5 mr-4 font-normal"
                :class="{ '!font-bold': currentActive === 'profile' }"
              >
                Profile
              </span>
            </div>
          </router-link>
        </li>
        <li class="py-1">
          <router-link
            to="/"
            class="p-3 inline-block hover:bg-gray-200 focus:bg-gray-300 cursor-pointer rounded-full h-14"
          >
            <div class="flex">
              <MoreIcon class="inline h-7" />

              <span class="hidden lg:inline text-xl ml-5 mr-4 font-normal">
                More
              </span>
            </div>
          </router-link>
        </li>
      </ul>
      <button
        class="bg-sky-500 h-13 w-13 lg:w-56 rounded-full my-4 text-white mx-1"
      >
        <TweetIcon class="inline lg:hidden" />
        <span class="hidden lg:inline font-bold text-lg">Tweet</span>
      </button>
    </nav>
  </div>
</template>

<script setup lang="ts">
import TweetIcon from "../icons/TweetIcon.vue";
import HomeIconFill from "../icons/HomeIconFill.vue";
import HomeIconOutline from "../icons/HomeIconOutline.vue";
import ExploreIconFill from "../icons/ExploreIconFill.vue";
import ExploreIconOutline from "../icons/ExploreIconOutline.vue";
import NotificationsIconFill from "../icons/NotificationsIconFill.vue";
import NotificationsIconOutline from "../icons/NotificationsIconOutline.vue";
import MessagesIconFill from "../icons/MessagesIconFill.vue";
import MessagesIconOutline from "../icons/MessagesIconOutline.vue";
import BookmarksIconFill from "../icons/BookmarksIconFill.vue";
import BookmarksIconOutline from "../icons/BookmarksIconOutline.vue";
import ListsIconFill from "../icons/ListsIconFill.vue";
import ListsIconOutline from "../icons/ListsIconOutline.vue";
import ProfileIconFill from "../icons/ProfileIconFill.vue";
import ProfileIconOutline from "../icons/ProfileIconOutline.vue";
import MoreIcon from "../icons/MoreIcon.vue";
import { useRoute } from "vue-router";
import { computed } from "@vue/reactivity";

const route = useRoute();
const currentActive = computed(() => route.name?.toString().toLowerCase());
</script>
