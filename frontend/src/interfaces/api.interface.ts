export interface Dataframe {
  labels: string[],
  correlation: number,
  x: string[],
  y: number[],
}

export type Route = "/analyze/hydration-impact" | "/analyze/1" | "/analyze/2" | "/analyze/3" | "/analyze/4"

export interface ApiResponse {
  result_dataframe: unknown,
  dataframe: Dataframe[]
}