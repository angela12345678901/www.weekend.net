class AntiLoopBot:
    def __init__(self):
        self.assistant_history = []
        self.repeat_count = 0

    def process_chat(self, user_message, assistant_response):
        # Limpia espacios y saltos de línea para evitar bypass sencillos
        cleaned_user = " ".join(user_message.strip().split())
        
        # Verifica si el mensaje del usuario coincide con alguna respuesta previa del asistente
        if cleaned_user in self.assistant_history:
            self.repeat_count += 1
            if self.repeat_count > 3:
                return "ALERTA: ¡Bucle detectado y bloqueado! Detén las repeticiones."
        else:
            self.repeat_count = 0  # Resetea si el usuario rompe el patrón
            
        # Registra la respuesta actual del asistente en el historial
        cleaned_assistant = " ".join(assistant_response.strip().split())
        self.assistant_history.append(cleaned_assistant)
        return assistant_response
