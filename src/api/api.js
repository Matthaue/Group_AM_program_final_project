import request from "../utils/request";

export const api = {
  // 登录接口
  login(data) {
    return request({
      url: "/auth/login",
      method: "post",
      data,
    });
  },

  getDeviceList(params) {
    return request({
      url: "/setting/list",
      method: "get",
      params,
    });
  },


  saveDevice(data) {
    return request({
      url: "/setting",
      method: "post",
      data,
    });
  },

  updateDevice(data, setting_id) {
    return request({
      url: `/setting/${setting_id}`,
      method: "put",
      data,
    });
  },



  deleteDevice(setting_id) {
    return request({
      url: `/setting/${setting_id}`,
      method: "delete",
    });
  },




};
