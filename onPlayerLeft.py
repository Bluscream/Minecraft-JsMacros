if __name__ == "": from JsMacrosAC import * #Autocomplete, not necessary

builder = Chat.createTextBuilder()\
    .append("[\u00A7l\u00A7c+\u00A7r] \u00A77")\
    .append(event.player.getName())\
    .withShowTextHover(Chat.createTextHelperFromString(event.player.getUUID()))
Chat.log(builder.build())