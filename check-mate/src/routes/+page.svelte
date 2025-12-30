<script lang="ts">
	// PARCHE SVELTE 5: Usamos $state para reactividad moderna
	let query = $state("");
	let loading = $state(false);
	let results = $state<any>(null);
	let error = $state<string | null>(null);

	async function handleVerify() {
		if (!query) return;
		loading = true;
		error = null;
		results = null; 

		try {
			// PARCHE: Usamos 127.0.0.1 para asegurar la ruta local
			const response = await fetch('http://127.0.0.1:5000/api/verify', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ query })
			});
			
			if (!response.ok) throw new Error("Servidor no responde");

			const data = await response.json();
			if (data.success) {
				results = data.results;
			} else {
				error = "Hubo un problema con la API: " + data.error;
			}
		} catch (err) {
			error = "No se pudo conectar con el servidor Python. ¿Ejecutaste 'python app.py'?";
		} finally {
			loading = false;
		}
	}

	function getRatingClass(rating: string) {
		if (!rating) return '';
		const r = rating.toLowerCase();
		if (r.includes('fals') || r.includes('fake') || r.includes('mentira')) return 'veredicto-falso';
		if (r.includes('verdader') || r.includes('true') || r.includes('cierto')) return 'veredicto-verdadero';
		if (r.includes('engaños') || r.includes('dudos') || r.includes('parcial')) return 'veredicto-dudoso';
		return '';
	}
</script>

<main class="container">
	<header>
		<h1>🛡️ CheckMate</h1>
		<p>Verificación Híbrida: Google + Chile + Web</p>
	</header>

	<section class="search-section">
		<input 
			type="text" 
			bind:value={query} 
			placeholder="Pega un link o escribe tu duda..." 
			onkeydown={(e) => e.key === 'Enter' && handleVerify()}
			disabled={loading}
		/>
		<button onclick={handleVerify} disabled={loading}>
			{loading ? 'Buscando...' : 'Analizar'}
		</button>
	</section>

	{#if error}
		<article class="error-card">
			<strong>Error:</strong> {error}
		</article>
	{/if}

	{#if results}
		<div class="accordion-group">
			
			<details>
				<summary>
					<span>🇨🇱 Medios Chilenos</span>
					<span class="count">{results.chile.length}</span>
				</summary>
				<div class="content">
					{#each results.chile as item}
						<article class="resultado-card">
							<small>{item.claimReview[0].publisher.name}</small>
							<h4>{item.claimReview[0].title}</h4>
							<a href={item.claimReview[0].url} target="_blank" class="btn-link">Ver reporte</a>
						</article>
					{:else}
						<p class="empty-msg">No se hallaron registros en prensa chilena.</p>
					{/each}
				</div>
			</details>

			<details>
				<summary>
					<span>🌍 Google Fact Check</span>
					<span class="count">{results.google.length}</span>
				</summary>
				<div class="content">
					{#each results.google as item}
						<article class="resultado-card {getRatingClass(item.claimReview[0].textualRating)}">
							<small>{item.claimReview[0].publisher.name}</small>
							<h4>{item.claimReview[0].title}</h4>
							<mark class="badge">{item.claimReview[0].textualRating}</mark>
						</article>
					{:else}
						<p class="empty-msg">Sin resultados en Google.</p>
					{/each}
				</div>
			</details>

			<details>
				<summary>
					<span>🔍 Búsqueda Web General</span>
					<span class="count">{results.web.length}</span>
				</summary>
				<div class="content">
					{#each results.web as item}
						<article class="resultado-card web-item">
							<h4>{item.claimReview[0].title}</h4>
							<p>{item.claimReview[0].textualRating}</p>
							<a href={item.claimReview[0].url} target="_blank">Visitar sitio</a>
						</article>
					{:else}
						<p class="empty-msg">Sin resultados en la web abierta.</p>
					{/each}
				</div>
			</details>

		</div>
	{/if}
</main>

<style>
	:global(body) { background-color: #f1f5f9; margin: 0; font-family: system-ui, sans-serif; }
	.container { max-width: 850px; margin: 0 auto; padding: 2rem; }
	header { text-align: center; margin-bottom: 2rem; }
	header h1 { color: #2563eb; font-size: 2.5rem; margin-bottom: 0.5rem; }

	.search-section { display: flex; gap: 1rem; margin-bottom: 2rem; background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
	input { flex: 1; padding: 0.8rem; border-radius: 8px; border: 1px solid #e2e8f0; font-size: 1rem; }
	button { background: #2563eb; color: white; border: none; padding: 0.8rem 2rem; border-radius: 8px; cursor: pointer; font-weight: bold; }
	button:disabled { background: #94a3b8; }

	details { background: white; border-radius: 12px; margin-bottom: 1rem; padding: 1rem; border: 1px solid #e2e8f0; }
	summary { cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-weight: bold; }
	.count { background: #2563eb; color: white; padding: 2px 12px; border-radius: 20px; font-size: 0.8rem; }

	.resultado-card { border-top: 1px solid #f1f5f9; padding: 1.2rem 0; border-left: 6px solid #cbd5e1; padding-left: 1rem; margin-top: 1rem; }
	.veredicto-falso { border-left-color: #ef4444; }
	.veredicto-verdadero { border-left-color: #22c55e; }
	.veredicto-dudoso { border-left-color: #f59e0b; }

	.badge { border-radius: 20px; padding: 4px 12px; font-size: 0.8rem; font-weight: bold; color: white; background: #64748b; }
	.veredicto-falso .badge { background: #ef4444; }
	.veredicto-verdadero .badge { background: #22c55e; }

	.error-card { background: #fee2e2; color: #b91c1c; padding: 1rem; border-radius: 10px; border: 1px solid #fecaca; margin-bottom: 1rem; }
	.btn-link { color: #2563eb; text-decoration: none; font-weight: bold; font-size: 0.9rem; }
	.empty-msg { color: #94a3b8; font-style: italic; margin-top: 1rem; }
</style>