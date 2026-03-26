package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ControlPart  {

  private String id;
  private String name;
  private String ns;
  private String class;
  private String title;
  private String prose;
  private List<ControlPart> parts;
  private List<Property> props;
  private List<Link> links;

}