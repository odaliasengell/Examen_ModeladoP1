# Etapa de construcción
FROM node:18 AS builder

# Instalación de pnpm globalmente
RUN npm install -g pnpm

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de definición de dependencias
COPY package.json pnpm-lock.yaml ./

# Instalación de dependencias del proyecto
RUN pnpm install

# Copia el resto de archivos del proyecto
COPY . .

# Compilación del proyecto
RUN pnpm run build

# Etapa de ejecución
FROM node:18-alpine AS runner

# Instalación de pnpm en el entorno final
RUN npm install -g pnpm

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de definición de dependencias
COPY package.json pnpm-lock.yaml ./

# Instalación de dependencias en modo producción
RUN pnpm install --prod

# Copia solo los artefactos de la compilación desde el contenedor anterior
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/next.config.ts ./next.config.ts

# Expone el puerto de la aplicación
EXPOSE 8080

# Comando de inicio
CMD ["pnpm", "start"]
