import notification from "ant-design-vue/es/notification";

export const API = {
  Generate: "auth/phone/generate/",
  Validate: "auth/phone/validate/",
  Info: "users/info/",
  Logout: "users/logout/",
  Users: "users/",
  Groups: "groups/",
  Permissions: "permissions/",
  Contracts: "contracts/",
  Address: "address/",
  Skills: "skills/",
  WorkTimes: "worktimes/"
};

export function updateSuccess(res) {
  notification.success({
    message: "Update Success"
  });
}

export function updateFailed(res) {
  notification.error({
    message: "Update Failed!"
  });
}

export function createSuccess(res) {
  notification.success({
    message: "Create Success"
  });
}

export function createFailed(res) {
  notification.error({
    message: "Create Failed!"
  });
}

export function deleteSuccess(res) {
  notification.success({
    message: "Delete Success"
  });
}

export function deleteFailed(res) {
  notification.error({
    message: "Delete Failed!"
  });
}
