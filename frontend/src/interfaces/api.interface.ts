export interface Dataframe {
  title: string,
  labels: string[],
  correlation: number,
  x: string[],
  y: number[],
}

export type Route = "/analyze/hydration-impact" | "/analyze/experience-impact" | "/analyze/duration-impact" | "/analyze/3" | "/analyze/4"

export interface ApiResponse {
  result_dataframe: unknown,
  dataframe: Dataframe[]
}