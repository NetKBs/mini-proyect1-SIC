export interface Dataframe {
  labels: string[],
  correlation: number,
  x: string[],
  y: number[],
}

export type Route = "/analyze/hydration-impact" | "/analyze/experience-impact" | "/analyze/duration-impact" | "/analyze/bmi-impact" | "/analyze/frecuency-impact"

export interface ApiResponse {
  result_dataframe: unknown,
  dataframe: Dataframe[]
}