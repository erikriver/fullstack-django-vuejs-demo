<template>
  <div id="app">
    <GoogleMapLoader
      :apiKey="apiKey"
    >
      <template slot-scope="{ google }">
        <GMap
          :mapConfig="mapConfig"
          :google="google">

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
import axios from 'axios';
import GoogleMapLoader from './components/GoogleMapLoader.vue';
import GMap from './components/GMap.vue';
import GoogleMapMarker from './components/GoogleMapMarker.vue';

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
    GMap,
    GoogleMapMarker
  },
  data() {
    return {
      places: [],
      apiKey: 'AIzaSyDZWKixyVZvyUo8nFJGSiR2lPyyPgQg35w',
      loading: true
    };
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/properties/?at=52.517626,13.377864')
      .then(response => {
        this.places = response.data,
        console.log(response.data),
        console.log(this.places)
      })
      .catch(error => {
        console.log(error)
      })
      .finally(() => this.loading = false)

    //this.fetchPlaces()
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
            lat: 52.517626, lng: 13.377864,
        },
      };
    },
  },
  // methods: {
  //           fetchPlaces() {
  //                 fetch('http://127.0.0.1:8000/api/properties/?at=52.517626,13.377864')
  //                     .then(response => response.json())
  //                     .then(data => this.places = data)
  //                     .catch(error => console.error(error))
  //                 console.log("Help!!!")
  //                 console.log(this.places)

  //           }
  // }
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
