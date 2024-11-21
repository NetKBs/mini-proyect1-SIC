import { ApiResponse, Route } from "../interfaces/api.interface";

export class Api {
  async get(route: Route): Promise<ApiResponse> {
    try {
      const response = await fetch(route)
      const data: ApiResponse = await response.json()
      return data
    } catch (error) {
      console.log(error);
      return {} as ApiResponse
    }
  }
}