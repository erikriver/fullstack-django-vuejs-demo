<template>
  <div class="wrapper">
    <div :id="id">
      <h1>{{ marker.title }}</h1>
      <p>{{ marker.address }}</p>
      <button class="button">Book</button>
    </div>
  </div>
</template>

<style>
  .wrapper {display: none}
  .button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 10px 26px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
</style>

<script>
import Icon from '../assets/icon_default.svg';
export default {
  props: {
    google: {
      type: Object,
      required: true,
    },
    map: {
      type: Object,
      required: true,
    },
    marker: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      point: null,
      infoWindow: null,
    };
  },
  mounted() {
    this.point = new this.google.maps.Marker({
      position: this.marker.location,
      map: this.map,
      title: JSON.stringify(this.marker.title),
      icon: Icon,
    });
    this.point.addListener('click', () => this.showPopup(this.map, this.point));
  },
  computed: {
    id() {
      return `info_${this.marker.id}`;
    },
  },
  methods: {
    showPopup(map, point) {
      if (!this.infoWindow) {
        this.infoWindow = new this.google.maps.InfoWindow({
          content: document.getElementById(this.id),
        });
      }
      this.infoWindow.open(map, point);
    },
  },
};
</script>