<template>
  <div>
    <div class="google-map" ref="googleMap"></div>
    <template v-if="Boolean(this.map)">
      <slot :map="map" />
    </template>
  </div>
</template>

<script>
export default {
  props: {
    google: {
      type: Object,
      required: true
    },
    mapConfig: Object
  },
  data() {
    return {
      map: null
    };
  },
  mounted() {
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      const mapContainer = this.$refs.googleMap;
      this.map = new this.google.maps.Map(mapContainer, this.mapConfig);
    }
  }
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
