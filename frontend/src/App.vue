<template>
  <div id="app">
    <div class="header">
      <a href="#" class="logo">Company Logo</a>
      <div class="header-right">
        <a class="menu" href="#">
          <svg
            width="16"
            height="10"
            viewBox="0 0 16 10"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M0 9H16"
              stroke="#222222"
              stroke-width="1.5"
              stroke-linejoin="round"
            />
            <path
              d="M0 1H16"
              stroke="#222222"
              stroke-width="1.5"
              stroke-linejoin="round"
            />
          </svg>
        </a>
      </div>
    </div>

    <GoogleMapLoader :apiKey="apiKey">
      <template slot-scope="{ google }">
        <GMap :mapConfig="mapConfig" :google="google">
          <template slot-scope="{ map }">
            <GoogleMapMarker
              v-for="marker in places"
              :key="marker.id"
              :marker="marker"
              :google="google"
              :map="map"
            />
          </template>
        </GMap>
      </template>
    </GoogleMapLoader>
  </div>
</template>

<script>
import axios from "axios";
import GoogleMapLoader from "./components/GoogleMapLoader.vue";
import GMap from "./components/GMap.vue";
import GoogleMapMarker from "./components/GoogleMapMarker.vue";

const mapSettings = {
  clickableIcons: false,
  streetViewControl: false,
  panControlOptions: false,
  gestureHandling: "cooperative",
  mapTypeControl: false,
  zoom: 15,
  zoomControlOptions: {
    style: "SMALL"
  },
  minZoom: 2,
  maxZoom: 16
};

export default {
  name: "App",
  components: {
    GoogleMapLoader,
    GMap,
    GoogleMapMarker
  },
  data() {
    return {
      places: [],
      apiKey: "AIzaSyDZWKixyVZvyUo8nFJGSiR2lPyyPgQg35w",
      loading: true
    };
  },
  mounted() {
    axios
      .get("http://test.rivera.pro/api/properties/?at=52.517626,13.377864")
      .then(response => {
        (this.places = response.data), console.log(this.places);
      })
      .catch(error => {
        console.log(error);
      })
      .finally(() => (this.loading = false));
  },
  computed: {
    markers() {
      return this.places.map(item => ({
        id: item.id,
        title: item.title,
        position: item.position,
        address: item.address
      }));
    },

    mapConfig() {
      return {
        ...mapSettings,
        center: {
          lat: 52.517626,
          lng: 13.377864
        }
      };
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.header {
  overflow: hidden;
  background-color: #e5e4e0;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 15px 10px;
}

.header a {
  float: left;
  color: black;
  text-align: center;
  text-decoration: none;
  font-size: 14px;
}

.header-right {
  float: right;
  padding: 0px 35px;
}
</style>
