with open('public/index.html', 'r') as f:
    content = f.read()

dummy_maker = "{ id: 'test_1', emoji: '🧪', title: 'Test Maker', description: 'Test Description', systemPrompt: '' },"
content = content.replace("officialMakers: [", "officialMakers: [" + dummy_maker)

with open('public/index.html', 'w') as f:
    f.write(content)
