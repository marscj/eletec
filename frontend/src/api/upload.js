import {
  API,
  deleteSuccess,
  deleteFailed,
  uploadSuccess,
  uploadFailed
} from "./index";
import { axios } from "@/utils/request";

export function getUploads(parameter) {
  return axios({
    url: API.Upload,
    method: "get",
    params: parameter
  });
}

export function upload(data) {
  return axios({
    url: API.Upload,
    method: "post",
    data: data
  })
    .then(uploadSuccess)
    .catch(uploadFailed);
}

export function deleteUpload(pk) {
  return axios({
    url: API.Upload + `${pk}/`,
    method: "delete"
  })
    .then(deleteSuccess)
    .catch(deleteFailed);
}
