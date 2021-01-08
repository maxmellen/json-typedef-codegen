
using System;

using System.Collections.Generic;

using System.Text.Json;

using System.Text.Json.Serialization;

namespace JtdCodegenE2E
{
    /// <summary>
    /// To specify a constraint specific to Polygons, it is useful to
    /// introduce the concept of a linear ring:
    /// 
    /// o  A linear ring is a closed LineString with four or more positions.
    /// 
    /// o  The first and last positions are equivalent, and they MUST contain
    ///     identical values; their representation SHOULD also be identical.
    /// 
    /// o  A linear ring is the boundary of a surface or the boundary of a
    ///     hole in a surface.
    /// 
    /// o  A linear ring MUST follow the right-hand rule with respect to the
    ///     area it bounds, i.e., exterior rings are counterclockwise, and holes
    ///     are clockwise.
    /// 
    /// Note: the [GJ2008] specification did not discuss linear ring winding
    /// order.  For backwards compatibility, parsers SHOULD NOT reject Polygons
    /// that do not follow the right-hand rule.
    /// 
    /// Though a linear ring is not explicitly represented as a GeoJSON geometry
    /// type, it leads to a canonical formulation of the Polygon geometry type
    /// definition as follows:
    /// 
    /// For Polygons with more than one of these rings, the first MUST be the
    /// exterior ring, and any others MUST be interior rings.  The exterior ring
    /// bounds the surface, and the interior rings (if present) bound holes
    /// within the surface.
    /// </summary>

    [JsonConverter(typeof(LinearRingJsonConverter))]
    public class LinearRing
    {
        /// <summary>
        /// The underlying data being wrapped.
        /// </summary>
        public IList<Position> Value { get; set; }
    }

    public class LinearRingJsonConverter : JsonConverter<LinearRing>
    {
        public override LinearRing Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
        {
            return new LinearRing { Value = JsonSerializer.Deserialize<IList<Position>>(ref reader, options) };
        }

        public override void Write(Utf8JsonWriter writer, LinearRing value, JsonSerializerOptions options)
        {
            JsonSerializer.Serialize<IList<Position>>(writer, value.Value, options);
        }
    }
}