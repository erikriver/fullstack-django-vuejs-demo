<template>
  <div id="app">
    <GoogleMapLoader
      :apiKey="apiKey"
    >
      <template slot-scope="{ google }">
        <GMap
          :mapConfig="mapConfig"
          :google="google">
        </GMap>
      </template>
    </GoogleMapLoader>
  </div>
</template>

<script>
import GoogleMapLoader from './components/GoogleMapLoader.vue';
import GMap from './components/GMap.vue';

const mapSettings = {
  clickableIcons: false,
  streetViewControl: false,
  panControlOptions: false,
  gestureHandling: 'cooperative',
  mapTypeControl: false,
  zoom: 15,
  zoomControlOptions: {
    style: 'SMALL',
  },
  minZoom: 2,
  maxZoom: 16,
};

export default {
  name: 'App',
  components: {
    GoogleMapLoader,
    GMap
  },
  data() {
    return {
      apiKey: 'AIzaSyDZWKixyVZvyUo8nFJGSiR2lPyyPgQg35w',
    };
  },
  computed: {
    mapConfig() {
      return {
        ...mapSettings,
        center: {
            lat: 52.517626, lng: 13.377864,
        },
      };
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
