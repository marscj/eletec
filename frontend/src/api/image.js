import {
  API,
  deleteSuccess,
  deleteFailed,
  uploadSuccess,
  uploadFailed
} from "./index";
import { axios } from "@/utils/request";

export function getImages(parameter) {
  return axios({
    url: API.Images,
    method: "get",
    params: parameter
  });
}

export function updateImage(pk, data) {
  return axios({
    url: API.Images + `${pk}/`,
    method: "put",
    data: data
  });
}

export function uploadImage(data) {
  return axios({
    url: API.Images,
    method: "post",
    data: data
  })
    .then(uploadSuccess)
    .catch(uploadFailed);
}

export function deleteImage(pk) {
  return axios({
    url: API.Images + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
