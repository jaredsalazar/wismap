export default function SelectionPreview({ item }) {
  if (!item) return null

  const image = Array.isArray(item.images) ? item.images[0] : null

  return (
    <div className="selection-preview" aria-live="polite">
      {image ? (
        <img src={image} alt={`${item.id} ${item.name || 'product'}`} loading="lazy" />
      ) : (
        <div className="selection-preview-empty">No product image available</div>
      )}
      <div className="selection-preview-caption">
        <strong>{item.id}</strong>
        {item.name && <span>{item.name}</span>}
      </div>
    </div>
  )
}

