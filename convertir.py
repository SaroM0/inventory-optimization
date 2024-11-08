import pandas as pd

def recortar_csv(csv_file, output_file, proportion=1/3):
    print("Leyendo el archivo CSV...")  # Print para depuración
    # Leer el archivo CSV completo
    df = pd.read_csv(csv_file)
    print(f"Archivo CSV leído correctamente con {len(df)} filas y {len(df.columns)} columnas.")
    
    # Calcular el número de filas basado en la proporción
    num_rows = int(len(df) * proportion)
    df_recortado = df.iloc[:num_rows]
    print(f"Archivo recortado a {proportion*100:.0f}%: {num_rows} filas seleccionadas.")
    
    # Guardar el nuevo archivo recortado
    df_recortado.to_csv(output_file, index=False)
    print(f"Archivo recortado guardado correctamente como '{output_file}'.")

# Llamar a la función con el nombre del archivo CSV de entrada y el archivo CSV de salida
recortar_csv("./data/df_ventas_concat.csv", "./data/df_ventas_1_tercio.csv", proportion=1/5)
