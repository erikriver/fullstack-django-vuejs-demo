<template>
  <div>
    <template v-if="Boolean(this.google)">
      <slot
        :google="google"
      />
    </template>
  </div>
</template>

<script>

import GoogleMapsApiLoader from 'google-maps-api-loader';

export default {
  name: 'GoogleMapLoader',
  props: {
    apiKey: String,
  },

  data() {
    return {
      google: null,
    };
  },

  async mounted() {
    const googleMapApi = await GoogleMapsApiLoader({
      apiKey: this.apiKey,
    });
    this.google = googleMapApi;
  },
};
</script>

<style>
.google-map {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  background: #fff;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>
